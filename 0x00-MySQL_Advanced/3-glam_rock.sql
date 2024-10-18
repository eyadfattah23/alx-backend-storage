-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (IFNULL(CAST(split AS UNSIGNED), 2022) - CAST(formed AS UNSIGNED) ) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
