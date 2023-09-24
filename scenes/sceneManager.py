"""
    This function handle scene 
    @getScene return name of scene and scene number
    @setScene change current scene
    @run start the scene if paused
"""
class GameSceneManager:
    def __init__(self, currentScene, scenes):
        self.currentScene = currentScene
        self.scenes = scenes
        self.state = "pause"

    def getScene(self):
        return {"name": self.currentScene, "scene": self.scenes[self.currentScene]}

    def setScene(self, scene):
        self.currentScene = scene

    def run(self):
        if self.state == "pause":
            self.state = "running"
            self.scenes[self.currentScene].start()
        else:
            self.scenes[self.currentScene].run()
