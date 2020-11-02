from .views import frontend


def setup_routes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/contacts', frontend.contact_section)
    app.router.add_route('GET', '/post', frontend.post)
