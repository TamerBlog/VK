import vk_api

api = vk_api.VkApi(token='59a00a084b79f323e5c6f3b95908f9a6e8f29aed1fb011f4707b907eb5e1c5115a36f640772685d9e7226')

def main():
	try:
		for x in range(0, 1000):
			api.method("wall.createComment", {"owner_id":666935196, "post_id": 46057, "message":'&#12;'})
			print(x)
	except:
		main()

main()