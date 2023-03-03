#pragma once

#include <thread>
#include <mutex>
#include <deque>
#include <optional>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <memory>
#include <iostream>
#include <chrono>
#include <NetCommon.cpp>

#ifdef _WIN32
#define _WIN32_WINNT 0x0A00
#endif
#define ASIO_STANDALONE
#include <asio.hpp>
#include <asio/ts/buffer.hpp>
#include <asio/ts/internet.hpp>
#include <asio/ip/tcp.hpp>

vector<string> Message(string MessageContent, string Destination); // Funktion für die Erstellung von einer Nachricht

using namespace asio;
using namespace std;
using ip::tcp;