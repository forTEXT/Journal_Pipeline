return {
  {
    Meta = function(m)
      if m.origdate then
        local origdate = pandoc.utils.stringify(m.origdate)
        m.origdate = pandoc.MetaMap({
          ["iso"] = origdate,
          ["year"] = string.sub(origdate, 1, 4),
          ["month"] = string.sub(origdate, 6, 7),
          ["day"] = string.sub(origdate, 9, 10),
        })
        return m
      end
    end,
  },
}
