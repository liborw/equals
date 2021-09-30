
local api = vim.api
local uv = vim.loop

local M = {}

function M.setup()
  api.nvim_set_keymap('n', 'ee', ':lua require("equals").buffer()', {expr = true, noremap = true})
end

-- apply single equals line edit
local function update_line(line, col_start, col_end, text)

  -- TODO: Move buf to some upper function
  local buf = api.nvim_get_current_buf()

  -- If col_end is equal to -1 then we want to overwrite the rest of the line
  if col_end == -1 then
    local lines = api.nvim_buf_get_lines(buf, line, line+1, true)
    col_end = #lines[1]
  end

  -- Add space before the result
  for i = 1, #text do
    text[i] = " " .. text[i]
  end

  -- update lines
  api.nvim_buf_set_text(buf, line, col_start, line, col_end, text)
end


local function buffer_to_string()
  local buf = api.nvim_get_current_buf()
  local text = api.nvim_buf_get_lines(buf, 0, -1, false)
  return table.concat(text, '\n')
end

local function parse_stdout(err, output)
  if err then error("err: " .. err) end
  local updates = vim.fn.json_decode(output)

  for i = 1, #updates do
    local u = updates[i]
    update_line(u.line_num, u.col_start, u.col_end, u.value)
  end

  print(string.format("%d lines updates", #updates))
end

local function close_handle(handle)
    if handle and not handle:is_closing() then handle:close() end
end

local function buf_to_stdin(cmd, args, handler)
    local output = ""
    local stderr_output = ""

    local handle_stdout = vim.schedule_wrap(function(err, chunk)
        if err then print("stdout error: " .. err) end

        if chunk then output = output .. chunk end

        if not chunk then
            handler(stderr_output ~= "" and stderr_output or nil, output)
        end
    end)

    local function handle_stderr(err, chunk)
        if err then print("stderr error: " .. err) end
        if chunk then stderr_output = stderr_output .. chunk end
    end

    local stdin = uv.new_pipe(true)
    local stdout = uv.new_pipe(false)
    local stderr = uv.new_pipe(false)
    local stdio = {stdin, stdout, stderr}

    local handle
    handle = uv.spawn(cmd, {args = args, stdio = stdio}, function()
        stdout:read_stop()
        stderr:read_stop()

        close_handle(stdin)
        close_handle(stdout)
        close_handle(stderr)
        close_handle(handle)
    end)

    uv.read_start(stdout, handle_stdout)
    uv.read_start(stderr, handle_stderr)

    stdin:write(buffer_to_string(), function() stdin:close() end)
end

function M.buffer()

  local buf = api.nvim_get_current_buf()
  local filetype = api.nvim_buf_get_option(buf, 'filetype')
  local cmd = 'equals'
  local args = {'-l', filetype, '-u'}
  buf_to_stdin(cmd, args, parse_stdout)

end

return M
