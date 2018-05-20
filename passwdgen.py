# -*- coding: utf-8 -*-
import fire

class PasswordGenerator(object):

    def generate(self):
        print("Generate")
        return None

    def validate(self):
        print("Validate")
        return False


if __name__ == '__main__':
    fire.Fire(PasswordGenerator)
