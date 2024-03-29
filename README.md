<br/>
<p align="center">
    <img src="https://i.ibb.co/wpBWPSY/68747470733a2f2f66696c65732e636174626f782e6d6f652f326265326b352e6a7067.jpg" alt="logo" />
</p>
<p align="center">
    <a href="LICENSE" target="_blank">
        <img src="https://img.shields.io/github/license/tybantarnusa/switchmypresence" alt="license" />
    </a>
</p>
<br />

__SwitchMyPresence__ is a Nintendo Switch RPC, an easy-to-use __Discord Rich Presence integration application__ to show what game you are playing right now on __Nintendo Switch__.

<p align="center">
    <img src="https://i.ibb.co/MCJtjS6/68747470733a2f2f66696c65732e636174626f782e6d6f652f6334766737372e706e67.png" alt="app">
</p>

The game can be easily selected from the list or input your own title if it's not included yet. After launching the presence, the game that you has selected will be displayed on Discord.

<p align="center">
    <img src="https://i.ibb.co/mHdnrKh/image.png" alt="result">
</p>

## Running from Source
For now this application is only tested on Windows. But you can try to run this on other OS and tell me if it works or not.

### Prerequisites
- [Git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/) with Pip

Please install all the requirements before proceeding into the next steps.

### Steps
1. Clone and get into the directory:
    ```{bash}
    git clone https://github.com/tybantarnusa/switchmypresence.git
    cd switchmypresence
    ```

2. Install dependencies:
    ```{bash}
    py -m pip install -r requirements.txt
    ```

3. Run the code:
    ```
    py src/app.py
    ```

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated. However, we are still writing the documentation for contributing.

Though, we always welcome your Pull Requests or Issues now even if the documentation is not finished yet. Just do what you want.

## License
Distributed under the GPL-3.0 License. See [LICENSE](https://github.com/tybantarnusa/switchmypresence/blob/master/LICENSE) for more information.