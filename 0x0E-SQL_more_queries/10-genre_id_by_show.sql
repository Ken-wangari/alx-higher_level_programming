-- List all shows with at least one genre linked using EXISTS
SELECT title, genre_id
FROM tv_shows
WHERE EXISTS (
    SELECT 1
    FROM tv_show_genres
    WHERE tv_shows.id = tv_show_genres.show_id
)
ORDER BY title ASC, genre_id ASC;

