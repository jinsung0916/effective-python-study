# BETTER WAY 18 __missing__을 사용해 키에 따라 다른 디폴트 값을 생성하는 방법을 알아두라

class Pictures(dict):
    def __missing__(self, key):
        value = self.__open_picture(key)
        self[key] = value
        return value

    def __open_picture(self, profile_path):
        try:
            return open(profile_path, 'a+b')
        except OSError:
            print(f'경로를 열 수 없습니다: {profile_path}')
            raise

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
