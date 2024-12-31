
import logging
logger = logging.getLogger('file_log')
from disease.models import book_table,whatsapp_table,data_table
from home.models import video_table
from pathy.models import effective_table
from members.models import members_table
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.exceptions import ObjectDoesNotExist


def fetchlinks(request):
    try:
        all_links = []
        logger.info("Fetching Links")

        # Query data from different models
        book_table_data = book_table.objects.all()
        whatsapp_table_data = whatsapp_table.objects.all()
        data_table_data = data_table.objects.all()
        video_table_data = video_table.objects.all()
        effective_table_data = effective_table.objects.all()
        members_table_data = members_table.objects.all()

        # Iterate through Book Table data
        for item in book_table_data:
            link = item.buy_link
            all_links.append({'link': link, 'source_table': "book_table", 'item_id': item.id})

        for item in whatsapp_table_data:
            link = item.link
            all_links.append({'link': link, 'source_table': "whatsapp_table", 'item_id': item.id})

        for item in data_table_data:
            link = item.link
            all_links.append({'link': link, 'source_table': "data_table", 'item_id': item.id})

        for item in video_table_data:
            link = item.ytplaylist_link
            all_links.append({'link': link, 'source_table': "video_table", 'item_id': item.id})

        for item in effective_table_data:
            link = item.link
            all_links.append({'link': link, 'source_table': "effective_table", 'item_id': item.id})

        for item in members_table_data:
            link = item.linkedin_url
            all_links.append({'link': link, 'source_table': "members_table", 'item_id': item.id})

        # Prepare JSON response
        response_data = {'links': all_links}  # Using 'links' as the key for the list of links

        return JsonResponse(data=response_data, status=200)

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Requested data does not exist.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def checkresponse(request):
    logger.info("Checking Response")

    json_data = json.loads(request.body.decode('utf-8'))
    links_list = json_data.get('links', [])
    response_data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate'
    }

    for link_data in links_list:
        link = link_data.get('link', '')
        source_table = link_data.get('source_table', '')
        item_id = link_data.get('item_id', '')
        try:
            response = requests.get(link, headers=headers, timeout=10)
            status_code = response.status_code
            if response.ok:
                if status_code == 200:
                    status = "Site is accessible"
                else:
                    status = f"Status code: {status_code}"
            else:
                if status_code == 404:
                    status = "Site not found (404 Error)"
                elif status_code == 403:
                    status = "Access forbidden (403 Error)"
                elif status_code == 500:
                    status = "Internal server error (500 Error)"
                elif status_code == 503:
                    status = "Service unavailable (503 Error)"
                elif status_code == 401:
                    status = "Unauthorized access (401 Error)"
                elif status_code == 400:
                    status = "Bad request (400 Error)"
                elif status_code == 429:
                    status = "Too many requests (429 Error)"
                else:
                    status = f"Error: {status_code} {response.reason}"

        except requests.Timeout:
            status_code = None
            status = "Error: Connection timed out (timeout exceeded)"
        except requests.ConnectionError:
            status_code = None
            status = "Error: Connection error"
        except Exception as e:
            status_code = None
            status = f"Error: {str(e)}"

        response_data.append({"link": link, "status_code": status_code, "status": status, 'source_table': source_table, 'item_id': item_id})

    return JsonResponse(data=response_data, status=200, safe=False)

@csrf_exempt
def checkoccurrence(request):
    try:
        if request.method != 'GET':
            return JsonResponse(data={"message": f"method {request.method} does not exist"}, status=405)

        json_data = json.loads(request.body.decode('utf-8'))
        link_to_check = json_data.get('link')

        all_links = {}

        # Query data from different models
        book_table_data = book_table.objects.all()
        whatsapp_table_data = whatsapp_table.objects.all()
        data_table_data = data_table.objects.all()
        video_table_data = video_table.objects.all()
        effective_table_data = effective_table.objects.all()
        members_table_data = members_table.objects.all()

        # Populate all_links dict
        for item in book_table_data:
            link = item.buy_link
            all_links[link] = {'source_table': "book_table", 'item_id': item.id}

        # Include or not ?
        for item in whatsapp_table_data:
            link = item.link
            all_links[link] = {'source_table': "whatsapp_table", 'item_id': item.id}

        for item in data_table_data:
            link = item.link
            all_links[link] = {'source_table': "data_table", 'item_id': item.id}

        for item in video_table_data:
            link = item.ytplaylist_link
            all_links[link] = {'source_table': "video_table", 'item_id': item.id}

        for item in effective_table_data:
            link = item.link
            all_links[link] = {'source_table': "effective_table", 'item_id': item.id}

        is_present = link_to_check in all_links

        return JsonResponse({'is_present': is_present})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data provided.'}, status=400)

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Requested data does not exist.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)











