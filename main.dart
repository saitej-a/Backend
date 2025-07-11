import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
  // Optional: call registerUser directly for testing
  registerUser(
    username: 'testuser',
    password: 'password123',
    role: 'STUDENT',
    firstName: 'Ravi',
    lastName: 'Kiran',
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Registration Test',
      home: Scaffold(
        appBar: AppBar(title: Text('Register API Tester')),
        body: Center(child: Text('Check your console for response.')),
      ),
    );
  }
}

Future<void> registerUser({
  required String username,
  required String password,
  required String role,
  required String firstName,
  required String lastName,
}) async {
  final url = Uri.parse('https://didactic-fiesta-pxq49jvgv7r27rv-8000.app.github.dev/api/register/'); // Replace with real URL

  final body = jsonEncode({
    'username': username,
    'password': password,
    'role': role,
    'first_name': firstName,
    'last_name': lastName,
  });

  try {
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: body,
    );

    if (response.statusCode == 201 || response.statusCode == 200) {
      print('✅ Registration successful!');
      print(response.body);
    } else {
      print('❌ Registration failed with status ${response.statusCode}');
      print('Response: ${response.body}');
    }
  } catch (e) {
    print('❌ Error: $e');
  }
}
