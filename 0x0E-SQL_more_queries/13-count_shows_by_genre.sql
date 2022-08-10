-- lists all genres from the database hbtn_od_tvshows
-- along with the number of shows linked to each
-- does not display genres without linked shows
-- records ordered by descending number of shows linked
SELECT G.name as genre,
	COUNT(*) AS number_of_shows
FROM tv_genres as G
INNER JOIN tv_show_genres AS t
	ON g.id = t.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
