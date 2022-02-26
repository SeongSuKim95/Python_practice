# Repository for practice some python skills


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
    

## 2. Concept


  

