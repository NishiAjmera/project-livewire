# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tool execution and handling for Gemini Multimodal Live Proxy Server
"""

import logging
import aiohttp
from typing import Dict, Any
# from config.config import CLOUD_FUNCTIONS
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

async def execute_tool(tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a tool based on name and parameters by calling the corresponding cloud function"""
    if tool_name == "get_weather":
        logger.info(f"Returning mock response for tool: {tool_name}")
        city = params.get('city', 'Unknown City')
        return {
            "city": city,
            "temperature": 20,
            "description": "partly cloudy",
            "humidity": 75,
        }