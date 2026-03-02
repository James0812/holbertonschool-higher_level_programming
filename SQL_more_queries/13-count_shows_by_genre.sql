SELECT g.name AS genre,
       COUNT(tsg.tv_show_id) AS number_of_shows
FROM tv_show_genres tsg
JOIN genres g ON tsg.genre_id = g.id
GROUP BY g.name
HAVING COUNT(tsg.tv_show_id) > 0
ORDER BY number_of_shows DESC;
