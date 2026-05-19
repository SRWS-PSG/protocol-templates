-- Highlight protocol-template editing aids:
--   1. Blockquotes that start with "Note" / "*Note*" / 「メンター」など → class "note"
--   2. Inline [english label / 日本語ラベル: ...] placeholders → class "placeholder"
-- Both are mapped to the same light-blue color via CSS (HTML) and the
-- "Note" / "Placeholder" custom styles in reference.docx (DOCX).

local function starts_with_note(blockquote)
  for _, blk in ipairs(blockquote.content) do
    if blk.t == "Para" or blk.t == "Plain" then
      local s = pandoc.utils.stringify(blk)
      -- strip leading markdown emphasis markers / spaces
      s = s:gsub("^[%s%*_]+", "")
      if s:match("^[Nn]ote") or s:match("^メンター") then
        return true
      end
      return false  -- only inspect the first textual block
    end
  end
  return false
end

function BlockQuote(el)
  if starts_with_note(el) then
    return pandoc.Div(el.content,
      pandoc.Attr("", {"note"}, {["custom-style"] = "Note"}))
  end
end

-- Walk inline lists and wrap [ ... ] placeholders in a Span.
-- A placeholder is detected as a balanced bracket pair that contains
-- both a "/" and a ":" (matches "[english / 日本語: 内容]"), so we don't
-- accidentally wrap citation keys like [@page2021prisma] or generic
-- bracketed text.
local function wrap_placeholders(inlines)
  local out = pandoc.List({})
  local i, n = 1, #inlines
  while i <= n do
    local x = inlines[i]
    if x.t == "Str" then
      local lb = x.text:find("%[", 1, false)
      if lb then
        -- emit prefix before "["
        if lb > 1 then
          out:insert(pandoc.Str(x.text:sub(1, lb - 1)))
        end
        -- collect inlines until we see a Str containing "]"
        local collected = pandoc.List({})
        local rest = x.text:sub(lb + 1)  -- after the "["
        local found_close = false
        local close_tail = ""

        local function scan(text)
          local rb = text:find("%]", 1, false)
          if rb then
            if rb > 1 then
              collected:insert(pandoc.Str(text:sub(1, rb - 1)))
            end
            close_tail = text:sub(rb + 1)
            found_close = true
          else
            if #text > 0 then collected:insert(pandoc.Str(text)) end
          end
        end

        scan(rest)
        local j = i + 1
        while not found_close and j <= n do
          local y = inlines[j]
          if y.t == "Str" then
            scan(y.text)
          else
            collected:insert(y)
          end
          j = j + 1
        end

        if found_close then
          local inner_text = pandoc.utils.stringify(collected)
          if inner_text:find("/") and inner_text:find(":") then
            out:insert(pandoc.Span(collected,
              pandoc.Attr("", {"placeholder"}, {["custom-style"] = "Placeholder"})))
          else
            -- not a placeholder: re-emit verbatim
            out:insert(pandoc.Str("["))
            for _, c in ipairs(collected) do out:insert(c) end
            out:insert(pandoc.Str("]"))
          end
          if #close_tail > 0 then
            out:insert(pandoc.Str(close_tail))
          end
          i = j
        else
          -- no closing bracket found: emit the original "[" + rest verbatim
          out:insert(pandoc.Str(x.text))
          i = i + 1
        end
      else
        out:insert(x)
        i = i + 1
      end
    else
      out:insert(x)
      i = i + 1
    end
  end
  return out
end

function Para(el)
  el.content = wrap_placeholders(el.content)
  return el
end

function Plain(el)
  el.content = wrap_placeholders(el.content)
  return el
end

function Header(el)
  el.content = wrap_placeholders(el.content)
  return el
end
