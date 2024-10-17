-- Lists all Glam rock bands, ranked by their longevity until 2022
SELECT 
    band_name,
    IFNULL(2022 - formed, 0) - IFNULL(NULLIF(split, 0) - formed, 0) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC;
