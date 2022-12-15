class MyService:
    def download_img(self, url: str):
        if url:
            return True

        raise Exception("url is not valid")
