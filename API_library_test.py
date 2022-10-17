import requests

class PSD_API:
    # GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS

    @staticmethod
    def get_from_server():
        API_ENDPOINT = "http://api.open-notify.org/astros.json"
        response = requests.get(API_ENDPOINT)
        # print("This is a get request from backend API endpoint")
        print(response.status_code)
        print("Response: " + response.text)
    
    @staticmethod    
    def post_to_server():
        API_ENDPOINT = "https://pastebin.com/api/api_post.php"
        API_KEY = "5oEwtdzBW0FwLN6tNJdOSH3An9M8y3Kr"
    
        data_to_post = '''
        {
            "numofcar":20,
            "emptyParkingSpotscore":0.89,
        }
        '''
        data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':data_to_post,
        'api_paste_format':'json'}

        r = requests.post(url = API_ENDPOINT, data = data)
    
        pastebin_url = r.text
        print("Pasted text at : %s"%pastebin_url)
        # print("This is a post to backend API endpoint")


# PSD_API().get_from_server()
PSD_API().post_to_server()