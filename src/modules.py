import json
import base64
import glob
import multiprocessing
import os
import sys
import requests
import shutil
import tiktoken
from git import Repo
from halo import Halo

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import CSVLoader, UnstructuredWordDocumentLoader, UnstructuredEPubLoader, \
    PDFMinerLoader, UnstructuredMarkdownLoader, TextLoader


