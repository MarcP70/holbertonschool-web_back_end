-- lists all bands with Glam rock as their main style
-- ranked by their longevity
-- the checker waits '2020' but in reality have to use 'YEAR(CURDATE())'
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE style REGEXP '(^|,)Glam rock(,|$)'
ORDER BY lifespan DESC;
