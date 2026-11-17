class Singleton:
    __instance = None

    # 객체를 하나만 생성
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    # count 초기화
    def __init__(self):
        if not hasattr(self, "count"):
            self.count = 0

    # 싱글톤 인스턴스 반환
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()

        return Singleton.__instance


# 1. 인스턴스 두 번 가져오기
a = Singleton.get_instance()
b = Singleton.get_instance()

# 2. 동일한 객체인지 확인
print("동일 인스턴스 확인:", a is b)

# 3. 상태 공유 확인
a.count = 10

print("a의 count:", a.count)
print("b의 count:", b.count)

# 4. 직접 생성해도 같은 객체인지 확인
c = Singleton()

print("직접 생성 시 동일 인스턴스:", a is c)