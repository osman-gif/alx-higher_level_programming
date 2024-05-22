--  script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_genre.genre_id 
FROM tv_show_genres tv_shows
LEFT JOIN tv_shows tv_genre
ON tv_shows.show_id = tv_genre.id 
ORDER BY tv_genre.title, tv_shows.genre_id ASC;
