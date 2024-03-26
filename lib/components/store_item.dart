import 'package:flutter/material.dart';

class StoreItem extends StatelessWidget {
  final String title;
  final String description;
  final dynamic cost;
  final dynamic id;
  final dynamic follows;
  final dynamic fps;
  final Widget icon;

  const StoreItem({
    super.key,
    required this.title,
    required this.description,
    required this.cost,
    required this.id,
    required this.follows,
    required this.fps,
    required this.icon,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(2.0),
      child: ElevatedButton(
        onPressed: () => print(title),
        child: Row(
          children: [
            SizedBox(
              width: 60,
              height: 60,
              child: icon,
            ),
            Spacer(),
            Column(
              children: [
                Text(title),
                Text(description),
              ],
            ),
            Spacer(),
            Column(
              children: [
                Text('cost: $cost'),
                Text('follows: $follows'),
                Text('fps: $fps'),
              ],
            ),
            SizedBox(
              width: 20,
              height: 70,
            )
          ],
        ),
      ),
    );
  }
}
