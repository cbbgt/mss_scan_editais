from modules.scan_all_urls.scan_all_urls_presenter import scan_all_urls_presenter


def main(request):
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    request_json = request.get_json()
    action = request_json.get('action')
    if request_json.get('action') == '/scan':
        response = scan_all_urls_presenter(request=request)
        return (response[0], response[1], headers)
    return (f'Action {action} Not Found', 404, headers)
