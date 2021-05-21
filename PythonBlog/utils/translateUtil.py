
from typing import Callable, List, Dict, Any, Optional


def translateHList2Dict(
    h_list: List[str], *, 
    valuetype_translater: Optional[Callable] = None ) -> Dict[str, Any]:
    """
        将hgetall 返回的list转为dict
    """
    ret_dict = {}
    lis_length = len(h_list)

    if lis_length > 0:
        if lis_length % 2:
            raise ValueError("传入列表的长度要求为偶数 !!!!!!")
        for key_idx in range(0, lis_length, 2):
            if valuetype_translater is not None:
                value = valuetype_translater(h_list[key_idx + 1])
            else:
                value =h_list[key_idx + 1]
            ret_dict[h_list[key_idx]] = value
        
    return ret_dict


def translateHList2Zip(
    h_list: List[str], *,
    valuetype_translater: Optional[Callable] = None ) -> List[List[Any]]:
    """
        将hgetall 返回的list转为Zip数据格式类型 [(key, value), (key, value)]
    """
    ret_zip = []
    lis_length = len(h_list)
    if lis_length > 0:
        if lis_length % 2:
            raise ValueError("传入列表的长度要求为偶数 !!!!!!")
        for key_idx in range(0, lis_length, 2):
            if valuetype_translater is not None:
                value = valuetype_translater(h_list[key_idx + 1])
            else:
                value =h_list[key_idx + 1]
            ret_zip.append([h_list[key_idx], value])
    
    return ret_zip

 