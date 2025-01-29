import tiktoken

def encode_decode_demo(text):
    # 获取编码器
    enc = tiktoken.get_encoding("p50k_base")
    
    # 编码
    tokens = enc.encode(text)
    print(f"输入文本: {text}")
    print(f"编码后的tokens: {tokens}")
    
    # 解码
    decoded_text = enc.decode(tokens)
    print(f"解码后的文本: {decoded_text}")
    
    # 查看token数量
    print(f"Token数量: {len(tokens)}\n")
    
    # 显示每个token的实际内容
    print("Token ID 与内容对照:")
    print("-" * 30)
    for token_id in tokens:
        # 将单个token_id转为列表进行解码
        token_bytes = enc.decode([token_id])
        print(f"Token ID: {token_id:5d} | 内容: {repr(token_bytes)}")

# 测试示例
sample_text = "🥺"
encode_decode_demo(sample_text)