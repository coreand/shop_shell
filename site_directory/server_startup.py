def start_server(application, bot):
    import config
    from telebot import types
    from flask import request, render_template

    @application.route('/{}'.format(config.TOKEN), methods=['POST'])
    def parse_request():
        bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
        return '', 200

    @application.route('/')
    def parse_index():
        return render_template('index.html')

    @application.route('/about.html')
    def parse_about():
        return render_template('about.html')

    @application.route('/check.php')
    def parse_result():
        return "CHECKKK"

    bot.remove_webhook()
    from time import sleep
    sleep(1)
    bot.set_webhook(url="https://{}:{}/{}".format(config.WEBHOOK_HOST, config.WEBHOOK_PORT, config.TOKEN),
                    certificate=open(config.WEBHOOK_SSL_CERT, 'rb'))
    application.run(host=config.WEBHOOK_LISTEN, port=config.WEBHOOK_PORT)

