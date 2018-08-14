# -*- coding:utf-8 -*-
__author__ = 'Cliff Huang'
__date__ = '2018/8/8 13:49'

from django.forms.widgets import Textarea,Media
from django.conf import settings
from django.template import loader
from django.forms.utils import flatatt
from django.utils.html import conditional_escape
from django.utils.encoding import force_text
from . import settings as markdown_settings

class MarkdownWidget(Textarea):
    def __init__(self, *args, **kwargs):
        self.template = kwargs.pop(
            "template", markdown_settings.MARKDOWN_WIDGET_TEMPLATE)
        self.lib = markdown_settings.STATIC_URL + "markdown/lib/"
        self.width = kwargs.pop("width", "960")
        self.height = kwargs.pop("height", "540")
        self.syncScrolling = kwargs.pop("syncScrolling", "single")
        self.saveHTMLToTextarea = kwargs.pop("saveHTMLToTextarea", True)
        self.emoji = kwargs.pop("emoji", True)
        self.taskList = kwargs.pop("taskList", True)
        self.tocm = kwargs.pop("tocm", True)
        self.tex = kwargs.pop("tex", True)
        self.flowChart = kwargs.pop("flowChart", True)
        self.sequenceDiagram = kwargs.pop("sequenceDiagram", True)
        self.codeFold = kwargs.pop("codeFold", True)
        self.imageUpload = kwargs.pop("imageUpload", True)
        self.imageFormats = kwargs.pop("imageFormats", markdown_settings.MARKDOWN_IMAGE_FORMATS)
        self.imageUploadURL = kwargs.pop("imageUploadURL", markdown_settings.MARKDOWN_UP_IMAGE_URL)
        self.theme = kwargs.pop("theme", "light")
        self.previewTheme = kwargs.pop("previewTheme", "light")
        self.editorTheme = kwargs.pop("editorTheme", "paraiso-light")
        super(MarkdownWidget, self).__init__(*args, **kwargs)

    @property
    def media(self):
        return Media(
            css={'all':('{}{}'.format(settings.STATIC_URL, "markdown/css/editormd.css"),
                        '{}{}'.format(settings.STATIC_URL, "markdown/css/override_admin.css"),
                        )
                 },
            js=(
                '{}{}'.format(settings.STATIC_URL,"markdown/js/jquery.min.js"),
                '{}{}'.format(settings.STATIC_URL,"markdown/js/editormd.min.js"),
                '{}{}'.format(settings.STATIC_URL, "markdown/js/image_csrf_upload.js"),
            )
        )

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        final_attrs = self.build_attrs(attrs, {'name': name})

        if "class" not in final_attrs:
            final_attrs["class"] = ""
        final_attrs["class"] += " wmd-input"
        template = loader.get_template(self.template)

        # Compatibility fix:
        # see https://github.com/timmyomahony/django-pagedown/issues/42
        # imageFormats_str=','.join('"'+i+'"' for i in self.imageFormats)
        # imageFormats_str='['+imageFormats_str+']'
        markdown_conf={
            'width':self.width,
            'height':self.height,
            'syncScrolling': self.syncScrolling,
            'saveHTMLToTextarea'   : self.saveHTMLToTextarea,
            'emoji':self.emoji,
            'taskList':self.taskList,
            'tocm':self.tocm,
            'tex':self.tex,
            'flowChart':self.flowChart,
            'sequenceDiagram':self.sequenceDiagram,
            'codeFold':self.codeFold,
            'imageUpload':self.imageUpload,
            'imageFormats':self.imageFormats,
            'imageUploadURL':self.imageUploadURL,
            'theme': self.theme,
            'previewTheme': self.previewTheme,
            'editorTheme':self.editorTheme,

        }

        context = {
            "attrs": flatatt(final_attrs),
            "body": conditional_escape(force_text(value)),
            "id": final_attrs["id"],
            "marklib":self.lib,
            "markdownconf":markdown_conf,
        }
        return template.render(context)

