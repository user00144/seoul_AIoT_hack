import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from llama_index.llms.huggingface import HuggingFaceLLM
from config import BASE_MODEL


class LLMLoader:
    def __init__(self, system_prompt, query_wrapper_prompt):
        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
        self.stopping_ids = [self.tokenizer.eos_token_id, self.tokenizer.convert_tokens_to_ids("<|eot_id|>")]
        self.system_prompt = system_prompt
        self.query_wrapper_prompt = query_wrapper_prompt
        self.base_model = BASE_MODEL
    def load_llm(self):
        print("Loading LLM...")
        
        return HuggingFaceLLM(
                max_new_tokens=1024,
                system_prompt=self.system_prompt,
                query_wrapper_prompt=self.query_wrapper_prompt,
                tokenizer_name=self.base_model,
                model_name=self.base_model,
                device_map="auto",  # CPU에서 실행되도록 설정 (필요시 'auto'로 변경)
                stopping_ids=self.stopping_ids,
                )