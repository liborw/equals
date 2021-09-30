
local api = vim.api

local function setup()

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

  -- update lines
  api.nvim_buf_set_text(buf, line, col_start, line, col_end, text)
end


local function equals()

  local buf = api.nvim_get_current_buf()
  local filetype = api.nvim_buf_get_option(buf, 'filetype')

  -- TODO: Call equals
  local cmd = string.format("equals -l %s -u -", filetype)
  local f = assert(io.popen(cmd, 'r'))

  -- TODO: Process all updates

end


return {
  setup,
  update_line,
  equals
}
