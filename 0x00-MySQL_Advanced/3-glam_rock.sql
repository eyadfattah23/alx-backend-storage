-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (IFNULL(CAST(split AS UNSIGNED), 2022) - CAST(formed AS UNSIGNED) ) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;


-- SELECT band_name, (COALESCE(split, CAST(2022 AS YEAR)) - formed) AS dur, style
-- FROM metal_bands
-- WHERE style LIKE '%glam rock%'
-- ORDER BY lifespan DESC;
