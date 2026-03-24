# UTCS webring 

## how to join

1.  open a new issue and select the 'join the webring' template
2.  provide your website url and `@utexas.edu` email
3.  if your email is valid, you'll be automatically verified!

## how to leave

1.  open a new issue and select the 'leave the webring' template
2.  provide your website url
3.  the bot will comment a verification token for you to place on your site
4.  once the token is live on your homepage or at `/.well-known/utcs-webring.txt`, comment `/verify`
5.  if the token is found, your site will be automatically removed

after submitting your issue, copy and paste this HTML snippet into your
website's homepage where you want the webring navigation to appear. replace 
`YOUR_WEBSITE_URL` in the code below with your actual website link.

```html
<div style="text-align: left; margin: 30px 0;">
    <a href="https://utcs-webring.krisub.workers.dev/prev?from=YOUR_WEBSITE_URL">←</a> | 
    <a href="https://krisub.github.io/utcs-webring/"><strong>utcs-webring</strong></a> | 
    <a href="https://utcs-webring.krisub.workers.dev/next?from=YOUR_WEBSITE_URL">→</a>
</div>
```
