-- lista all shows contained in the database hbtn_0d_tvshows
-- displays NULL for shows without genres
-- recordes ordered by s.title and g.genre_id
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
	ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
