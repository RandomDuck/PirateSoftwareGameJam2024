import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:viral_hysteria/components/bigcard.dart';
import 'package:viral_hysteria/modules/topbar.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => ThemeController(),
      child: Consumer<ThemeController>(
        builder: (context, state, _) {
          return MaterialApp(
            title: 'Viral Hysteria',
            theme: ThemeData(
              useMaterial3: true,
              colorScheme: ColorScheme.fromSeed(seedColor: state.themeColor),
            ),
            home: TopPage(),
          );
        },
      ),
    );
  }
}

class ThemeController extends ChangeNotifier {
  Color themeColor = Colors.green;
  void newColorSeed(target) {
    switch (target) {
      case 0:
        themeColor = Colors.green;
      case 1:
        themeColor = Colors.deepOrange;
      case 2:
        themeColor = Colors.blue;
      case 3:
        themeColor = Colors.blueGrey;
      default:
        themeColor = Colors.green;
    }

    notifyListeners();
  }
}

class TopPage extends StatefulWidget {
  @override
  State<TopPage> createState() => _TopPageState();
}

class _TopPageState extends State<TopPage> {
  var selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    final themeController = Provider.of<ThemeController>(context);
    Widget page;
    ThemeData theme = Theme.of(context);

    switch (selectedIndex) {
      case 0:
        page = BigCard(text: 'hello');
      case 1:
        page = Placeholder();
      case 2:
        page = Placeholder();
      case 3:
        page = Placeholder();
      default:
        throw UnimplementedError('no widget for $selectedIndex');
    }

    return LayoutBuilder(builder: (context, constraints) {
      return Scaffold(
        body: Container(
          color: theme.colorScheme.primaryContainer,
          child: Column(
            children: [
              TopBar(),
              Expanded(
                child: page,
              ),
            ],
          ),
        ),
        bottomNavigationBar: BottomNavigationBar(
          selectedItemColor: theme.colorScheme.onPrimaryContainer,
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: 'Profile',
              backgroundColor: Colors.green,
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.chat),
              label: 'Quacker',
              backgroundColor: Colors.deepOrange,
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.newspaper),
              label: 'News',
              backgroundColor: Colors.blue,
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.storage),
              label: 'Store',
              backgroundColor: Colors.blueGrey,
            ),
          ],
          currentIndex: selectedIndex,
          onTap: (value) {
            setState(() {
              selectedIndex = value;
              themeController.newColorSeed(value);
            });
          },
        ),
      );
    });
  }
}
