import instaloader
import base64
import requests


def get_as_base64(url):

    return base64.b64encode(requests.get(url).content)

def get_user(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(
        L.context, username)

    profile_pic = profile.profile_pic_url
    username = profile.username
    followers = profile.followers
    following = profile.followees
    name = profile.full_name
    bio = profile.biography
    is_verified = profile.is_verified

    URL = profile_pic
    photo = get_as_base64(URL)
    # image = im.resize((250, 250), Image.ANTIALIAS)
    # photo = ImageTk.PhotoImage(image)

    data = {
        'username': username,
        'followers': followers,
        'following': following,
        'full_name': name,
        'bio': bio,
        'profile_pic': str(photo)[2:-1],
        'is_verified': is_verified
    }
    # print(is_verified)
    return data

