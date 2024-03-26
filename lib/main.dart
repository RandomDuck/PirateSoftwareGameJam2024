import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:viral_hysteria/components/bigcard.dart';
import 'package:viral_hysteria/modules/profile.dart';
import 'package:viral_hysteria/modules/store.dart';
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
        themeColor = Colors.purple;
      case 2:
        themeColor = Colors.deepOrange;
      case 3:
        themeColor = Colors.blue;
      case 4:
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
    bool hasDm = false;
    Icon dmIcon = hasDm ? Icon(Icons.mark_unread_chat_alt) : Icon(Icons.chat);

    switch (selectedIndex) {
      case 0:
        page = BigCard(
          title: 'Profile',
          child: Profile(),
        );
      case 1:
        page = BigCard(
          title: 'Direct messages',
          child: Placeholder(
            color: Colors.white,
          ),
        );
      case 2:
        page = BigCard(
          title: 'Quacker',
          child: Placeholder(
            color: Colors.white,
          ),
        );
      case 3:
        page = BigCard(
          title: 'News',
          child: Placeholder(
            color: Colors.white,
          ),
        );
      case 4:
        page = BigCard(
          title: 'Store',
          child: Store(),
        );
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
              icon: Icon(Icons.account_box),
              label: 'Profile',
              backgroundColor: Colors.green,
            ),
            BottomNavigationBarItem(
              icon: dmIcon,
              label: 'DMs',
              backgroundColor: Colors.purple,
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.style),
              label: 'Quacker',
              backgroundColor: Colors.deepOrange,
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.newspaper),
              label: 'News',
              backgroundColor: Colors.blue,
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.shopping_cart),
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
