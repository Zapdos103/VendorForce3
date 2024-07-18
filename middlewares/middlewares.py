def middleware_teste(get_response):
    # Código de inicialização do Middleware
    def middleware(request):
        # Aqui vai o código a ser exeutado antes da view
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

        response = get_response(request)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Aqui vai o código a ser executado depois da view

        return response

    return middleware