
import re



class HTMLUtil:

    @staticmethod
    def deleteArticleTag(source: str) -> str:
        """
            删除文章内的markdown

            @param source 需要过滤的文本
            @return 过滤后的内容
        """
        # 删除HTML 和 markdown标签
        pattern_1 = "!\\[\\]\\((.*?)\\)"
        pattern_2 = "<[^>]+>"
        source = re.sub(pattern_2, "", re.sub(pattern_1, "", source))
        
        return HTMLUtil.deleteTag(source)


    @staticmethod
    def deleteCommentTag(source: str) -> str:
        """
            删除评论内容标签
            @param source 需要进行剔除HTML的文本
            @return 过滤后的内容
        """
        # 保留图片标签
        source = re.sub("(?!<(img).*?>)<.*?>", "", source)
        
        return HTMLUtil.deleteTag(source)


    @staticmethod
    def deleteTag(source: str) -> str:
        # 删除 转义字符
        source = re.sub("&.{2,6}?;", "", source)
        # 删除script标签
        source = re.sub("<[\\s]*?script[^>]*?>[\\s\\S]*?<[\\s]*?\\/[\\s]*?script[\\s]*?>", "", source)
        # 删除上style标签
        source = re.sub("<[\\s]*?style[^>]*?>[\\s\\S]*?<[\\s]*?\\/[\\s]*?style[\\s]*?>", "")
        
        return source

    