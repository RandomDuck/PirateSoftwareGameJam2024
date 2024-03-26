import 'package:flutter/material.dart';
import 'package:viral_hysteria/components/store_item.dart';
import 'package:viral_hysteria/datasets/store_items.dart';

class Store extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ...storeItemList.map((e) => StoreItem(
              id: e['id'],
              title: e['title'],
              description: e['description'],
              cost: e['cost'],
              follows: e['follows'],
              fps: e['fps'],
              icon: e['icon'],
            ))
        //TODO: fix store navigator
      ],
    );
  }
}
