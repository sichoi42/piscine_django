#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self):
            super().__init__("incorrect behaviour.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = []
        if self.check_type(content) == False and content != None:
            raise self.ValidationError
        if type(content) == list:
            self.content = content
        elif content != None:
            self.content.append(content)
        if tag_type == 'double':
            self.tag_type = 'double'
        else:
            self.tag_type = 'simple'

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ''
        result += '<' + self.tag
        if str(self.attr) != "{}":
            result += self.__make_attr()
        if self.tag_type == 'simple':
            result += '/>'
        else:
            result += '>'
        if self.tag_type == 'double':
            result += self.__make_content()
            result += '</' + self.tag + '>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if (len(str(elem)) != 0):
                result += "{0}\n".format(elem)
        result = "  ".join(result.splitlines(True))
        if len(result.strip('\n')) == 0:
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    print(Elem('html', content=[Elem('head', content=Elem('title', content=Text("\"Hello ground!\""), tag_type='double'), tag_type='double'), Elem('body', content=[Elem('h1', content=Text("\"Oh no, not again!\""), tag_type='double'), Elem('img', attr={'src' : "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')], tag_type='double')], tag_type='double'))
