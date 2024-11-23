## Docker
1. 安裝docker
    根據官方文件安裝依賴的套件，再安裝docker和docker compose
    https://docs.docker.com/engine/install/ubuntu/
    
    如果執行時遇到權限問題，執行以下程序
    1. 建立一個docker group (可能已存在)
       ```console
       sudo groupadd docker
       ```
    2. 將使用者加入group
       ```console
       sudo usermod -aG docker $USER
       ```
    3. 登入group
       ```
       newgrp docker
       ```
        
2. 先下載一個起始image (要Dockerfile指定的版本)
    ```console
    docker pull <image_name>

    # 也可以在Dockerfile內寫上，讓docker自己下載
    FROM <image_name>
    ```
3. 建立image
    ```console
    docker build --rm -f {Dockerfile_path} -t {image_name} .
    # --rm	  建立完成後刪除連帶生成的容器
    # 不要忘記最後的點，最後的點可以替換成任何路徑
    ```
4. 建立container
    ```console
    docker run -itd --rm -v {local_folder}:{image_folder} {image_id / name}
    ```
    -it	讓docker分配一個虛擬終端給容器，並保持開啟
    --rm	停止容器時會自動自我刪除
    -v	用valumes模式與host分享資料 (可一次指定多個資料夾)
    -d	開啟後detech
    
5. 離開container後要查看運作中的container
    ```console
    docker ps
    ```
6. 進入運行中的container
    ```console
    docker exec -it {container_name} bash
    ```
7. 關閉container
    ```console
    docker stop {container_name}
    ```