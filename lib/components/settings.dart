import 'package:flutter/material.dart';

class Settings extends StatelessWidget {
  final MenuController menuCon = MenuController();
  final List<Widget> settingsList = [
    MenuItemButton(
      onPressed: () {
        print('Save');
      },
      child: Row(
        children: [Icon(Icons.save), Text('Save')],
      ),
    ),
    MenuItemButton(
      onPressed: () {
        print('Load');
      },
      child: Row(
        children: [Icon(Icons.input), Text('Load')],
      ),
    ),
    MenuItemButton(
      onPressed: () {
        print('Reset');
      },
      child: Row(
        children: [Icon(Icons.replay), Text('Reset')],
      ),
    ),
    MenuItemButton(
      onPressed: () {
        print('Quit');
      },
      child: Row(
        children: [Icon(Icons.power_settings_new), Text('Quit')],
      ),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Column(mainAxisAlignment: MainAxisAlignment.center, children: [
      MenuAnchor(
        controller: menuCon,
        menuChildren: settingsList,
        child: TextButton.icon(
            onPressed: () {
              if (menuCon.isOpen) {
                menuCon.close();
              } else {
                menuCon.open();
              }
            },
            icon: Icon(Icons.settings),
            label: Text('Settings')),
      ),
    ]);
  }
}
