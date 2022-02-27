# Repository for practice some python skills

# Python
 - https://uni2237.tistory.com/56
 - https://velog.io/@koyo/python-docs-6
 - https://velog.io/@gndan4/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B4%80%EB%A0%A8-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A3%BC%EC%9A%94-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
 - https://seongbindb.tistory.com/54
## 1. Vscode
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


  

