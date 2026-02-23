-- function to manually set the column width of tables
function Table(tbl)
    if #tbl.colspecs == 8 then
        print("Filter aktiv")

        -- column widths relative to textwidth
        -- local col_widths = {0.06, 0.08, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14} --geist beitrag
        -- manually adapted col widths
        -- col_widths = {0.05, 0.05, 0.1, 0.1, 0.15, 0.15, 0.15, 0.15} -- orig
        -- col_widths = {0.08, 0.05, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15} -- test smaller font
        -- col_widths = {0.06, 0.06, 0.08, 0.16, 0.18, 0.12, 0.15, 0.17} --hegel 04.08.25
        col_widths = {0.05, 0.06, 0.09, 0.18, 0.2, 0.14, 0.13, 0.13}
        --col_widths = {0.02, 0.03, 0.10, 0.16, 0.12, 0.1, 0.13, 0.14} --svenjas beitrag
        
        
        for i, colspec in ipairs(tbl.colspecs) do
            colspec[2] = col_widths[i]
        end

        return tbl
    end
end


    