import json

import web

import jssp_ga_main

urls = (
    "/",
    "jssp",
)
render = web.template.render("templates")
app = web.application(urls, globals())


class jssp:
    def GET(self):
        return render.jssp()

    def POST(self):
        data = (web.data()).decode()
        response = jssp_ga_main.my_ga(data)
        return json.dumps(response)


if __name__ == "__main__":
    app.run()
