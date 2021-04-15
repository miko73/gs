def __init__(self, user_agent, token_url_template, platform):
        self.user_agent = user_agent
        self.token_url_template = token_url_template
        self.platform = platform

        self.session = requests.Session()
        self.session.cookies = http.cookiejar.LWPCookieJar()
        if not os.path.exists(COOKIE_FILE):
            self.session.cookies.save(COOKIE_FILE)
        self.session.cookies.load(COOKIE_FILE, ignore_discard=True)
        self.session.headers = {"User-agent": user_agent}
        if os.path.exists(SESSION_FILE):
            self.load()
        else:
            self._state = {
                'api_key': None,
                'client_api_key': None,
                'token': None,
                'access_token': None,
                'access_token_expiry': None
            }
        self.login() 