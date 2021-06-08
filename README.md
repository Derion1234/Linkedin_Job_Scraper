# Linkedin Job Scraper
This is a Linkedin scraper!

Scrap jobs on linkedin that interest you, then saves them on a MySQL DB and, if this jobs are "recently released"(compares the obtained jobs with the jobs in DB) it will send you an HTML email with the information and a link to postulate.


## IMPORTANT

You will need a MySQL table with 5 columns:

1. job_title
2. company_name
3. job_image
4. job_url
5. job_release

![Screenshot from 2021-06-07 21-00-48](https://user-images.githubusercontent.com/72522721/121102366-c3af3b00-c7d3-11eb-99b1-ae8943b03789.png)
