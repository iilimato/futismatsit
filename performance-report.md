# Performance report

## Test data

Test data was generated with seed.py-file:

- Users: 1000
- Games: 100000
- Comments: 1000000

## Results without indexes

| Page | Time |
|------|------|
| Front page: / | 0.50 s |
| Game page: /game/ | 0.07–0.28 s |
| User page: /user/ | 0.02–0.08 s |
| Search: /find_game?query=Oulu | 0.34 s |


## Results with indexes

| Page | Time |
|------|------|
| Front page: / | 0.55 s |
| Game page: /game/ | 0.00–0.02 s |
| User page: /user/ | 0.00–0.02 s |
| Search:  /find_game?query=Oulu | 0.11 s |

## Results

Indexes improved game page load times a lot. The front page is still slow. This is probably because it loads all 100000 games. This can most likely be solved with pagination. I will do that next.

## Results with indexes and pagination

| Page | Time |
|------|------|
| Front page: / | 0.00–0.02 s |
| Front page (page 2): /2 | 0.00–0.02 s |
| Game page: /game/ | 0.00–0.02 s |
| User page: /user/ | 0.00–0.01 s |
| User page (page 2): /user/2/2 | 0.00–0.01 s |
| Search: /find_game?query=Oulu | 0.08 s |

## Conclusions

Adding pagination fixed the slowness of front page. All pages now load fast.
