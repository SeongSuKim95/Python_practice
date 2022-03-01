# Repository for practice some python skills

# Python
 - list
    - list.extend 와 list.append의 차이
 - copy
    - deepcopy   
 - Collections.defaultdict
    - collections.defaultdict는 딕셔너리(dictionary)와 거의 비슷하지만 key값이 없을 경우 미리 지정해 놓은 초기(default)값을 반환하는 dictionary
    - Example 
    ```python
    # 예제(1) - dict vs defaultdict
    # 1-1. 기본 딕셔너리
    import collections
    ex1 = {'a':1, 'b':2}
    print(ex1)
    print(ex1['c'])
    # 결과
    # {'b': 2, 'a': 1}
    # ----> 4 print(ex1['c'])
    # 5
    # 6  defaultdict의 초기값 생성
    # KeyError: 'c'
    
    # 1-2. collections.defaultdict
    # defaultdict의 초기값 생성
    def default_factory():
        return 'null'
    ex2 = collections.defaultdict(default_factory, a=1, b=2)
    print(ex2)
    print(ex2['c'])
    # 결과
    # defaultdict(<function default_factory at 0x10ab50bf8>, {'b': 2, 'a': 1})
    # null
    ```
    - collections.defaultdict(default_factory, key=value,...)는 default_factory 와 key1=value1,key2=value2,...,keyn=valuen 를 인자(factor)로 받는데, default_factory 는 defaultdict의 초기값을 지정하는 인자이다. 예제(2-1)에서 default_factory 인자를 넣어주지않으면 기본 딕셔너리와 마찬가지로 KeyError Exception 에러가 난다.
    ```python
    # 예제(2-1) - default_factory를 지정하지 않은 경우
    import collections

    ex2 = collections.defaultdict(a=1, b=2)
    print(ex2)
    print(ex2['c'])
    '''
    결과
    defaultdict(None, {'b': 2, 'a': 1})
    ----> 6 print(ex2['c'])

    KeyError: 'c'
    '''
    # 예제(2-1) - default_factory를 지정하지 않은 경우

    import collections

    def default_factory():
        return 'null'
    ex2 = collections.defaultdict(a=1, b=2)
    print(ex2)
    print(ex2['c'])
    '''
    결과
    defaultdict(<function default_factory at 0x10ab50c80>, {'b': 2, 'a': 1})
    null
    '''
    ```
    - default_factory인자는 메소드 형태의 값을 인자로 받는데, list(), int(), set()...나 사용자가 직접 메소드를 생성할 수 있다. 예제(3)은 default_factory를 list(), int(), set()로 지정했을 때의 초기값을 출력하는 예제이다.
    ```python
    # 예제(3) - 다양한 default_factory
    import collections
    # 3-1. list
    ex_list = collections.defaultdict(list, a=[1,2], b=[3,4])
    print(ex_list)
    print(ex_list['c'])
    '''
    결과
    defaultdict(<class 'list'>, {'b': [3, 4], 'a': [1, 2]})
    []
    '''
    # 3-2. set
    ex_set = collections.defaultdict(set, a={1,2}, b={3,4})
    print(ex_set)
    print(ex_set['c'])
    '''
    결과
    defaultdict(<class 'set'>, {'b': {3, 4}, 'a': {1, 2}})
    set()
    '''
    # 3-3. int
    ex_int = collections.defaultdict(int, a=1, b=2)
    print(ex_int)
    print(ex_int['c'])
    '''
    결과
    defaultdict(<class 'int'>, {'b': 2, 'a': 1})
    0
    '''
    ```

 - https://uni2237.tistory.com/56
 - https://velog.io/@koyo/python-docs-6
 - https://velog.io/@gndan4/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B4%80%EB%A0%A8-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A3%BC%EC%9A%94-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
 - https://seongbindb.tistory.com/54
# Vscode
-------------------
### About VsCode debugging
  - 참고 링크 [[LINK]](https://stackoverflow.com/questions/38623138/vscode-how-to-set-working-directory-for-debug)
  - Debugging interpreter의 경우 Conda로 생성한 Interpreter를 vscode 하단부에서 정해주면 경로를 알아서 잡는다.
  - .vscode의 launch.json 에서 debugging 에 대한 configuration을 설정할 수 있다.
  - launch.json 
    ```python
    {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Attention map debug",
            "type": "python",
            "request": "launch",
            "module": "vit_explain",
            "cwd": "${file}",
            "args": [
                "--image_path=./examples/input.png",
            ]
        }
    ]
    }
    ```
    -  name : Debug configuration의 이름
    -  cwd : Debugging이 실행될 root 경로
        - 설정하지 않을 경우 프로젝트 폴더의 root경로를 잡기 떄문에, file 간 module import가 필요할 경우 debugging이 실행되는 파일에서 다른 파일을 참조하지 못할 수도 있다.
        - 보통 debugging 파일의 경로를 설정해주면 되는데, import되는 파일에 따라서 적절하게 잡아주면 될듯
    -  module : debugging할 파일의 이름
        - 경로를 적는거라, 앞서 설정한 cwd에 맞춰서 적어주면 됨
    -  args : argument를 list 형식으로 적어주면 된다.
## 2. Concept
  - Factory 
  

  

