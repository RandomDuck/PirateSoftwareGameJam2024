import 'package:flutter/material.dart';
import 'package:viral_hysteria/components/score.dart';
import 'package:viral_hysteria/components/settings.dart';

class TopBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: SizedBox(
        height: 50,
        child: Row(
          children: [
            Expanded(
              child: Row(
                children: [ScoreBox()],
              ),
            ),
            Settings(),
          ],
        ),
      ),
    );
  }
}
