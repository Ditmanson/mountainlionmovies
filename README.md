# recommender

# Kanban Board:
https://github.com/users/gsmith177/projects/4/views/2

## Testing
Run command `pytest`

# Important references:
- [SSL](https://docs.digitalocean.com/support/how-do-i-install-an-ssl-certificate-on-a-droplet/)
- [Digital Ocean Django Setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
There's a handful of stuff that needs to be changed to fit our needs. If it's not obvious how to make it work with our stuff, send chat gpt both the provided code from the documentation and your applicable files and tree structure. Also! At the bottom there's instructions for chaning the file permissions for your static files, I can't tell you how long this was killing me. Because we are only using this droplet for the one applicaton, then you don't need kubernetes. Gunicorn creates multiple worker nodes that are good enough for this application.
